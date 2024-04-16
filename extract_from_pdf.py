import logging
import os.path

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation

# Set up logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# Function to execute the PDF extraction operation
def execute_pdf_extraction(pdf_file_path, output_zip_path):
    try:
        # Initialize base path
        base_path = "/content"

        # Set up credentials
        credentials = Credentials.service_principal_credentials_builder(). \
            with_client_id('141ccff7ee3c484f9ff44a90dfbde313'). \
            with_client_secret('p8e-TxvGtFskBLxgacGbXWi0_xOP1by8-dZh'). \
            build()

        # Create execution context
        execution_context = ExecutionContext.create(credentials)
        
        # Create extract PDF operation
        extract_pdf_operation = ExtractPDFOperation.create_new()

        # Set operation input from a source file
        source = FileRef.create_from_local_file(pdf_file_path)
        extract_pdf_operation.set_input(source)

        # Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        # Execute the operation
        result: FileRef = extract_pdf_operation.execute(execution_context)

        # Save the result to the specified location
        result.save_as(output_zip_path)
        print("Extraction successful!")

    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation")

# Execute the PDF extraction operation
execute_pdf_extraction("/home/vybhv/Downloads/NCT.pdf", "/mnt/32F6E6CAF6E68D83/kaam/MIRACL/metadata2.zip")


