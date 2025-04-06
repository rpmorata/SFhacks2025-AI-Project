
cd ../tools

python scrape.py "https://universe.roboflow.com/isha-dvf9n/skin_shade/browse?queryText=-class%3ABrown+-class%3ABlack&pageSize=1000&startingIndex=0&browseQuery=true" --folder white
python scrape.py "https://universe.roboflow.com/isha-dvf9n/skin_shade/browse?queryText=-class%3AWhite&pageSize=1000&startingIndex=0&browseQuery=true" --folder notwhite

python makedb.py
python populatedb.py


cd ../src 
python train.py

