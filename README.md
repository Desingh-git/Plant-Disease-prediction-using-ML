# Plant Disease Prediction using ML

Overview
--------
A simple Flask-based web app that predicts plant diseases from uploaded images using a pre-trained Keras model.

Repository structure
--------------------
- `app.py` - main Flask application (web UI and endpoints)
- `predict.py` - prediction helper (loads model and runs inference)
- `models/plant.h5` - trained Keras model used for prediction
- `templates/` - HTML templates (`upload.html`, `about.html`)
- `static/remedies.json` - mapping of disease -> remedies
- `uploads/` - uploaded images
- `summery.py` - (utility script)
- `requirment.txt` - Python dependencies (note spelling preserved)

Requirements
------------
- Python 3.8+ recommended
- Install dependencies:

```bash
pip install -r requirment.txt
```

Setup & Run
-----------
1. Ensure `models/plant.h5` is present (already included in this repo).
2. Install dependencies (see above).
3. Start the app:

```bash
python app.py
```

Usage
-----
- Open the web UI (default URL printed by the Flask server).
- Use the upload form (`upload.html`) to submit a leaf image.
- The app will classify the image and show the predicted disease and remedies from `static/remedies.json`.

Notes
-----
- If you modify or retrain the model, replace `models/plant.h5` and restart the app.
- The dependency file is named `requirment.txt` in this repo—update if you rename it to `requirements.txt`.

Contact
-------
If you'd like, I can also:
- run the app locally and verify endpoints
- update `requirment.txt` spelling and regenerate a clean `requirements.txt`
