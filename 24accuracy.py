#returns (accuracy, f1 score)
def accuracy(tp, fp, tn, fn):
    acc = (tp + tn) / (tp + tn + fp + fn)
    f1 = tp / (tp + 1/2 * (fp + fn))
    return acc, f1

print(accuracy(1,2,3,4))