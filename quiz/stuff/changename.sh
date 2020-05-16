#!/bin/bash
cd $1
rm -rf ../static/
mv assets/ ../static/
sed -i'.bs' -e 's|assets/|static/|g' *.html
rm -f *.html.bs
# sed -i'.bs' -e 's|"/static/img/|"img/|g' *.html
# rm -f *.html.bs
# sed -i'.bs' -e 's|<img src/*.png|imgz|g' *.html
#<img src="
#      {{ url_for('\static'\, filename='\
  #img/profile.png
#      '\) }}" height="{{query_img_height}}" width="{{query_img_width}}">

#+g' signup1.html > signup.html
# rm -f *.html.bs
