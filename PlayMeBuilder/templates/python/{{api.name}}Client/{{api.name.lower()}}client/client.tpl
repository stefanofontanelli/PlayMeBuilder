
import urllib
import urllib2

__all__ = []


class {{api.name}}(object):

    def __init__(self, api_key, api_secret):

        self.apikey = api_key
        self.apisecret = api_secret
        self.api_uri = '{{api.uri}}'
        if self.api_uri.endswith('/'):
            self.api_uri = self.api_uri[:-1]
        {% for entity in api.entities %}
        self.{{entity.name.lower()}} = {{entity.name}}(self)
        {% endfor %}

    def get(self, method, **params):
        """Call the API 'method' using 'params'.
        """
        query_string = '&'.join(['='.join([str(key), str(value)]) 
                                 for key, value in params.iteritems()
                                 if not value is None])
        url = '{0}/{1}?{2}'.format(self.api_uri, method, query_string)
        return urllib2.urlopen(url).read()

    def post(self, method, **params):
        """Call the API 'method' using 'params'.
        """
        values = {}
        for key, value in params.iteritems():

            if value is None:
                continue

            values[str(key)] = str(value)

        request = urllib2.Request('{0}/{1}'.format(self.api_uri, method), 
                                  urllib.urlencode(values))
        return urllib2.urlopen(request).read()

{% for entity in api.entities %}
class {{entity.name}}(object):

    def __init__(self, client):
        self._client = client

{% for method in entity.methods %}
    def {{method.name}}(self{% for field in method.request.fields['required'] %}, {{field.name}}{% endfor %}{% for field in method.request.fields['optional'] %}, {{field.name}}={{field.default}}{% endfor %}):
    {% if 'GET' in method.request.methods %}
        return self._client.get('{{entity.name.lower()}}.{{method.name}}'{% for field in method.request.fields['all'] %}, {{field.name}}={{field.name}}{% endfor %})
    {% elif 'POST' in method.request.methods %}
        return self._client.post('{{entity.name.lower()}}.{{method.name}}'{% for field in method.request.fields['all'] %}, {{field.name}}={{field.name}}{% endfor %})
    {% else %}
        return None
    {% endif %}
{% endfor %}

{% endfor %}
