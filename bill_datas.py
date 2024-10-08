def invoice_data(results, bill_data): #bill data for invoices
    for idx, invoice in enumerate(bill_data.documents):
        invoice_data = {}
        vendor_name = invoice.fields.get("VendorName")
        if vendor_name:
            invoice_data["Vendor Name"] = vendor_name.value
        
        vendor_address = invoice.fields.get("VendorAddress")
        if vendor_address:
            invoice_data["Vendor Address"] = vendor_address.value

        vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
        if vendor_address_recipient:
            invoice_data["Vendor Address Recipient"] = vendor_address_recipient.content

        customer_name = invoice.fields.get("CustomerName")
        if customer_name:
            invoice_data["Customer Name"] = customer_name.value

        customer_id = invoice.fields.get("CustomerId")
        if customer_id:
            invoice_data["Customer Id"] = customer_id.value

        customer_address = invoice.fields.get("CustomerAddress")
        if customer_address:
            invoice_data["Customer Address"] = customer_address.value

        customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
        if customer_address_recipient:
            invoice_data["Customer Address Recipient"] = customer_address_recipient.value

        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            invoice_data["Invoice Id"] = invoice_id.value

        invoice_date = invoice.fields.get("InvoiceDate")
        if invoice_date:
            invoice_data["Invoice Date"] = invoice_date.value

        invoice_total = invoice.fields.get("InvoiceTotal")
        if invoice_total:
            invoice_data["Invoice Total"] = invoice_total.value

        billing_address = invoice.fields.get("BillingAddress")
        if billing_address:
            invoice_data["Billing Address"] = billing_address.value

        billing_address_rec = invoice.fields.get("BillingAddressRecipient")
        if billing_address_rec:
            invoice_data["Billing Address Recipient"] = billing_address_rec.value

    results.append(invoice_data)
    return results
def reciept_data(results, bill_data):
    for idx, receipt in enumerate(bill_data.documents):
        receipt_data = {}

        receipt_type = receipt.doc_type
        if receipt_type:
            receipt_data["Receipt Type"] = receipt_type

        merchant_name = receipt.fields.get("MerchantName")
        if merchant_name:
            receipt_data["Merchant Name"] = merchant_name.value

        transaction_date = receipt.fields.get("TransactionDate")
        if transaction_date:
            receipt_data["Transaction Date"] = transaction_date.value


        subtotal = receipt.fields.get("Subtotal")
        if subtotal:
            receipt_data["Subtotal"] = subtotal.value

        tax = receipt.fields.get("TotalTax")
        if tax:
            receipt_data["Tax"] = tax.value

        tip = receipt.fields.get("Tip")
        if tip:
            receipt_data["Tip"] = tip.value

        total = receipt.fields.get("Total")
        if total:
            receipt_data["Total"] = total.value

    results.append(receipt_data)
    return results
def awb_data(results, bill_data):
    for idx, doc in enumerate(bill_data.documents):
        doc_data = {}

        shipping_address = doc.fields.get('shipping_address')
        if shipping_address.value is not None:
            doc_data["Shipping Address"] = shipping_address.value

        consignee_name = doc.fields.get('consignee_name')
        if consignee_name.value is not None:
            doc_data["Consignee Name"] = consignee_name.value

        shipper_name = doc.fields.get('shipper_name')
        if shipper_name.value is not None:
            doc_data["Shipper Name"] = shipper_name.value

        consignee_address = doc.fields.get('consignee_address')
        if consignee_address.value is not None:
            doc_data["Consignee Address"] = consignee_address.value

        airway_bill_number = doc.fields.get('airway_bill_number')
        if airway_bill_number.value is not None:
            doc_data["Airway Bill Number"] = airway_bill_number.value

        issuer = doc.fields.get('Issuer')
        if issuer.value is not None:
            doc_data["Issuer"] = issuer.value

        total_weight = doc.fields.get('total_weight')
        if total_weight.value is not None:
            doc_data["Total Weight"] = total_weight.value

        execution_date = doc.fields.get('execution_date')
        if execution_date.value is not None:
            doc_data["Execution Date"] = execution_date.value

        total_bill = doc.fields.get('total_bill')
        if total_bill.value is not None:
            doc_data["Total Bill"] = total_bill.value

        currency = doc.fields.get('currency')
        if currency.value is not None:
            doc_data["Currency"] = currency.value

        departure_airport = doc.fields.get('departure_airport')
        if departure_airport.value is not None:
            doc_data["Departure Airport"] = departure_airport.value

        destination_airport = doc.fields.get('destination_airport')
        if destination_airport.value is not None:
            doc_data["Destination Airport"] = destination_airport.value

        shipper_account_number = doc.fields.get('Shipper_account_number')
        if shipper_account_number.value is not None:
            doc_data["Shipper Account Number"] = shipper_account_number.value
        results.append(doc_data)
    return results
def packing_data(results, bill_data):
    for idx, doc in enumerate(bill_data.documents):
        doc_data = {}

        vendor_address = doc.fields.get('VendorAddress')
        if vendor_address.value is not None:
            doc_data["Vendor Address"] = vendor_address.value

        billing_address = doc.fields.get('BillingAddress')
        if billing_address.value is not None:
            doc_data["Billing Address"] = billing_address.value

        shipping_address = doc.fields.get('ShippingAddress')
        if shipping_address.value is not None:
            doc_data["Shipping Address"] = shipping_address.value

        vendor_name = doc.fields.get('VendorName')
        if vendor_name.value is not None:
            doc_data["Vendor Name"] = vendor_name.value

        invoice_date = doc.fields.get('InvoiceDate')
        if invoice_date.value is not None:
            doc_data["Invoice Date"] = invoice_date.value

        customer_name = doc.fields.get('CustomerName')
        if customer_name.value is not None:
            doc_data["Customer Name"] = customer_name.value

        shipping_date = doc.fields.get('shipping_date')
        if shipping_date.value is not None:
            doc_data["Shipping Date"] = shipping_date.value

        customer_email = doc.fields.get('customer_email')
        if customer_email.value is not None:
            doc_data["Customer Email"] = customer_email.value

        order_no = doc.fields.get('OrderNo')
        if order_no.value is not None:
            doc_data["Order Number"] = order_no.value

    results.append(doc_data)
    return results
