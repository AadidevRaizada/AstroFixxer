echo "Run copy(JSON.stringify(g_original)) in console of chrome as save as tags.json"
rm -f tags_filtered.json tags.pot astrofixxer.pot po/astrofixxer.pot
xgettext astrofixxer.html --keyword=_tr --output astrofixxer.pot || exit 1
python3 po/filter_tags.py || exit 1
json2po tags_filtered.json tags.pot || exit 1
msgcat -o po/astrofixxer.pot astrofixxer.pot tags.pot
rm -f tags_filtered.json tags.pot astrofixxer.pot 
if [ "$1" == "--update" ]
then
    for po in po/*.po
    do
        msgmerge -U $po po/astrofixxer.pot
    done
fi  
python3 po/tojson.py
