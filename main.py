from urllib import urlopen,unquote,quote
import re,os.path
from flask import Flask, request, Response
from jinja2 import Template, Environment, FileSystemLoader
import json
from werkzeug.contrib.fixers import ProxyFix



class api_response(Response):
    def __init__(self, response_obj, format, *args, **kwargs):
        headers = []
        super(api_response, self).__init__(*args, **kwargs)
        self.data = json.dumps(response_obj)
        self.mimetype = 'application/json'
        


APP_DIR = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(APP_DIR,'templates')
app = Flask(__name__)
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
STATIC_URL="/static1/"

def indexof(word,key):
    try:
        k=word.index(key)
        return k
    except(ValueError):
        return -1

def quality(link):
    if(indexof(link,"small")>=0):
        return "(240p)"
    elif(indexof(link,"medium")>=0):
        return "(360p)"
    elif(indexof(link,"large")>=0):
        return "(480p)"
    elif(indexof(link,"hd720")>=0):
        return "HD(720p)"
    elif(indexof(link,"hd1080")>=0):
        return "HD(1080p)"
    else:
        return "unknown quality"
def format(link):
    if(indexof(link,"webm")>=0):
        return "webm"
    elif(indexof(link,"flv")>=0):
        return "flv"
    elif(indexof(link,"mp4")>=0):
        return "mp4"
    elif(indexof(link,"3gpp")>=0):
        return "3gpp"
    else:
        return "unknown format"


@app.route('/')
def rethome():
	template = env.get_template('home.html')
        rendered = template.render()
        return rendered

	#return Response("web page down for maintenance");




@app.route('/ytdownloader',methods=['POST'])
def getlinks():
	url = request.args['url']
	webpage=urlopen(url).read()
	s1=webpage.index("<title>")
	s2=webpage[s1:].index("</title>")
	title=webpage[s1+7:s2+s1];
	#print webpage
	#print title
	p=re.compile('var swf =.*')
	p1=re.findall(p,webpage)
	q= unquote(unquote(p1[0]))
	#print q
	l=q.index("url_encoded_fmt_stream_map=")
	k=q[l:].index("u0026amp;")
	q= q[l:l+k]
	x=0
	links=[]
	while 1:
		try:
			n4=q.index(",itag=")
			q1 = q[0:n4]
			q = q[n4+2:]
			n1=q1.index("url=");
			try:
				n2=q1.index("codecs")
				n3=q1.index("fallba")
				links.append(q1[n1+4:n2-1]+"!"+q1[n3:].replace("sig","signature"));
			except(ValueError):
				links.append(q1[n1+4:].replace("sig","signature"));
				x=1
		except(ValueError):
			if(x==0):
				break
			else:
				x=0
	flinks={'title': title}
	for i in links:
		i=i+'&title='+quote(title)
		formats=format(i)
		qualit=quality(i)
		if('name' in flinks):
			flinks['name'].append(formats+" "+qualit)
			flinks['link'].append(i)
			flinks['format'].append(formats)
			#print formats+" "+qualit 
		else:
			flinks['name']=[formats+" "+qualit]
			flinks['link']=[i]
			flinks['format']=[formats]
	response=api_response(flinks,'json')
	return response


@app.route('/ytdownloader')
def index():
	ctx = {'STATIC': STATIC_URL}
	template = env.get_template('index.html')
	rendered = template.render(ctx)	
	return rendered

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
	app.run(port=8080,debug=True)
