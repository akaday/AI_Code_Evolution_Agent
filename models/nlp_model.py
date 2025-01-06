from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import torch

def analyze_code_comments(code):
    # Load pre-trained BERT model and tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    # Tokenize input code comments
    inputs = tokenizer(code, return_tensors='pt', truncation=True, padding=True, max_length=512)

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted class
    predictions = torch.argmax(outputs.logits, dim=1)

    # Map the predicted class to a label
    labels = ['negative', 'neutral', 'positive']
    result = labels[predictions.item()]

    return result
