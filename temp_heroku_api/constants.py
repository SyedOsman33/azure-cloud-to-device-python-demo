HTTP_ERROR_CODE = 500
HTTP_SUCCESS_CODE = 200
RESPONSE_STATUS = "status"
RESPONSE_DATA = "response"
RESPONSE_MESSAGE = "message"

UNAUTHORIZED_USER = "Invalid Login credentials"
TEXT_OPERATION_UNSUCCESSFUL = "Operation_Unsuccessful"
TEXT_OPERATION_SUCCESSFUL = "Operation_Successful"
# TEXT_SUCCESSFUL = "Operation Successful"
TEXT_SUCCESSFUL = "Record has been added successfully"
TEXT_EDITED_SUCCESSFUL = "Record has been modified successfully"
METHOD_DOES_NOT_EXIST = "The specified method does not exist"
DEFAULT_ERROR_MESSAGE = "There is some issue your request cannot be processed."
TEXT_PARAMS_MISSING = "Params are missing"
TEXT_PARAMS_INCORRECT = "Incorrect param"

ERROR_RESPONSE_BODY = {
    RESPONSE_STATUS: 500,
    RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE,
}
