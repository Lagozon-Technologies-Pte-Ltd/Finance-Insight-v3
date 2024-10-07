from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from azure.core.credentials import AzureKeyCredential
from io import BytesIO
from bill_datas import invoice_data, reciept_data, awb_data, packing_data
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Check if the uploads folder exists, if not, create it
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

endpoint = os.environ.get('endpoint')
key = os.environ.get('key')

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    service = request.form.get('service-select')
    input_method = request.form.get('input-method')
    if service == 'Invoices':
        poller_method = 'prebuilt-invoice'
    elif service == 'Receipts':
        poller_method = 'prebuilt-receipt'
    elif service == 'AWB':
        poller_method = 'finance_insight'
    elif service == 'Packing Slip':
        poller_method = 'packing_slip'
    
    elif service == 'COMPOSED':
        poller_method = 'composed_model'
    
    if input_method == 'file' and 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            with open(file_path, "rb") as fh:
                file_buf = BytesIO(fh.read())
            poller = document_analysis_client.begin_analyze_document(poller_method, file_buf)
    elif input_method == 'url':
        form_url = request.form.get('bill_url')
        if form_url:
            poller = document_analysis_client.begin_analyze_document_from_url(poller_method, form_url)
    else:
        return redirect(request.url)
    
    bill_data = poller.result()
    
    results = []
    if poller_method == 'prebuilt-invoice':
        results = invoice_data(results, bill_data)
    elif poller_method == 'prebuilt-receipt':
        results = reciept_data(results, bill_data)
    elif poller_method == 'finance_insight':
        results = awb_data(results, bill_data)                
    elif poller_method == 'packing_slip':
        results = packing_data(results, bill_data)
    elif poller_method == 'composed_model':
        for idx, doc in enumerate(bill_data.documents):
            doc_type = doc.doc_type
            if doc_type == "composed_model:finance_insight":
                results = awb_data(results,bill_data)
            elif doc_type == "composed_model:packing_slip":
                results = packing_data(results, bill_data)

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
