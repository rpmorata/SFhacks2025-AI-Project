
cd ../tools

python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3AAcne&pageSize=200&startingIndex=0&browseQuery=true" --folder acne
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3AChickenpox&pageSize=200&startingIndex=0&browseQuery=true" --folder chickenpox
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3AEczema&pageSize=200&startingIndex=0&browseQuery=true" --folder eczema
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3Amelanoma&pageSize=200&startingIndex=0&browseQuery=true" --folder melanoma
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3AMonkeypox&pageSize=200&startingIndex=0&browseQuery=true" --folder monkeypox
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3APimple&pageSize=200&startingIndex=0&browseQuery=true" --folder pimple
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3APsoriasis&pageSize=200&startingIndex=0&browseQuery=true" --folder psoriasis
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3ARingworm&pageSize=200&startingIndex=0&browseQuery=true" --folder ringworm
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3Avitiligo&pageSize=200&startingIndex=0&browseQuery=true" --folder vitiligo
python scrape.py "https://universe.roboflow.com/skin-disease-ysval/skin-disease-detection-s7zik/browse?queryText=class%3Awarts&pageSize=200&startingIndex=0&browseQuery=true" --folder warts
python scrape.py "https://universe.roboflow.com/dataset-skin/eczema-herpes/browse?queryText=class%3A%22normal+skin%22&pageSize=200&startingIndex=0&browseQuery=true" --folder normal
python scrape.py "https://universe.roboflow.com/dataset-skin/eczema-herpes/browse?queryText=class%3AImpetigo&pageSize=500&startingIndex=0&browseQuery=true" --folder impetigo
python scrape.py "https://universe.roboflow.com/iwa-2023/skin-disease-identification-ae3yb/browse?queryText=class%3Aherpes&pageSize=200&startingIndex=0&browseQuery=true" --folder herpes
python scrape.py "https://universe.roboflow.com/iwa-2023/skin-disease-identification-ae3yb/browse?queryText=class%3Ascabies&pageSize=200&startingIndex=0&browseQuery=true" --folder scabies
python scrape.py "https://universe.roboflow.com/zakiyya/kulit-bakar/browse?queryText=class%3A%22First-Degree%22&pageSize=200&startingIndex=0&browseQuery=true" --folder firstdegburns
python scrape.py "https://universe.roboflow.com/zakiyya/kulit-bakar/browse?queryText=class%3A%22Second-Degree%22&pageSize=200&startingIndex=0&browseQuery=true" --folder seconddegburns
python scrape.py "https://universe.roboflow.com/zakiyya/kulit-bakar/browse?queryText=class%3A%22Third-Degree%22&pageSize=200&startingIndex=0&browseQuery=true" --folder thirddegburns
python scrape.py "https://universe.roboflow.com/tigro/brusie/browse?queryText=-class%3ACuts+-class%3AEczema+-class%3ADTI+-class%3AFace+-class%3AFeet+-class%3AHand+-class%3Anull+-class%3ASkin+-class%3A%22stage-1%22&pageSize=200&startingIndex=0&browseQuery=true" --folder bruise
python scrape.py "https://universe.roboflow.com/fyp-jn6yw/dermatology-advisor-6zdqh/browse?queryText=class%3A%22Skin+Cancer%22&pageSize=200&startingIndex=0&browseQuery=true" --folder skincancer
python scrape.py "https://universe.roboflow.com/fyp-jn6yw/dermatology-advisor-6zdqh/browse?queryText=class%3A%22Urticaria+Hives%22&pageSize=200&startingIndex=0&browseQuery=true" --folder hives
python scrape.py "https://universe.roboflow.com/utm-zaimq/skin-diseases-bkejc/browse?queryText=class%3Aatopic&pageSize=200&startingIndex=0&browseQuery=true" --folder atopicdermatitis

python makedb.py
python populatedb.py


cd ../src 
python train.py

