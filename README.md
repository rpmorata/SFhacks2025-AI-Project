# SFhacks2025-AI-Project

## Quick Start

### Get data
```
cd tools
python scrape.py "<url>"
```

### Make and populate database (if it doesn't exist)
Make a database to store the images with their corresponding classifications

```
python makedb.py
```

Populate the database with collected and sorted data

```
python populatedb.py
```

### Train the model
```
cd ../src 
python train.py
```

### Inference the model with your own image
```
cd ..
python inference.py --image "myImage.jpg"
```

