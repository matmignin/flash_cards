#!/bin/bash
cd $1
rm -rf ../static/
mv assets/ ../static/
sed -i'.bs' -e 's+assets/+static/+g' *.html
rm -f *.html.bs
#sed 's+<img src="static/img/profile.png">+<img src="{{ url_for('\static'\, filename='\img/profile.png'\) }}" height="{{query_img_height}}" width="{{query_img_width}}">+g' signup1.html > signup.html
