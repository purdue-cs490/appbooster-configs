upstream django {
	server unix:///home/appbooster/host.socket;
}

# configuration of the server
server {
	# the port your site will be served on
	listen			80;
	# the domain name it will serve for
	server_name		mc18.cs.purdue.edu; # substitute your machine's IP address or FQDN
	charset			utf-8;

	# max upload size
	client_max_body_size 75M;   # adjust to taste

	# Django media
	location /media  {
		alias		/home/appbooster/host/media;  # your Django project's media files - amend as required
	}

	location /static {
		alias		/home/appbooster/host/static; # your Django project's static files - amend as required
	}

	# Finally, send all non-media requests to the Django server.
	location / {
		uwsgi_pass	django;
		include		/home/appbooster/host/uwsgi_params; # the uwsgi_params file you installed
	}

	# Deny access to public.
	location /app/private {
		uwsgi_pass	django;
		include		/home/appbooster/host/uwsgi_params;
		allow		127.0.0.1;
		allow		::1;
		deny		all;
	}
}
