import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


def exception_handler(def_value=None):
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as err:
                # logger.error(err, exc_info=True)
                return def_value

        return applicator
    return decorate


def generic_response(response_body, http_status=200, header_dict={}, mime='application/json'):
    msg = json.dumps(response_body, cls=DjangoJSONEncoder)
    resp = HttpResponse(msg, status=http_status, content_type=mime)
    for name, value in header_dict.items():
        resp[name] = value
    return resp


def get_data_param(request, key, default):
    if hasattr(request, 'data'):
        key = request.data.get(key, default)
        return key or default
    else:
        return default
