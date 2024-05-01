from rouge_score import rouge_scorer
from text_rank import sentences
from test import summary_ori




scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
num_samples = len(sentences) 


total_scores = {'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
                'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0}}

for i in range(num_samples):
    scores = scorer.score(sentences[i], summary_ori[i])
    for metric in ['rouge1', 'rougeL']:
        for measure, score_value in zip(['precision', 'recall', 'fmeasure'], scores[metric]):
            total_scores[metric][measure] += score_value

# Tính trung bình điểm
for metric in ['rouge1', 'rougeL']:
    for measure in ['precision', 'recall', 'fmeasure']:
        total_scores[metric][measure] /= num_samples

print("Average ROUGE scores:")
print(total_scores)
