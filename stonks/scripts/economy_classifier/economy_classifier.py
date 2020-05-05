import numpy as np
import joblib
import os


def article_classify(article: str, model_path=os.path.join(os.path.abspath(os.curdir)+'/economy_classifier/', 'economy_classifier_RF.sav'),
                     convect_path=os.path.join(os.path.abspath(os.curdir)+ '/economy_classifier/', 'economy_classifier_CV.sav'),
                     diff_coef=.1) -> list:
    """
    Gets an article text and model path and countvector path (which is used for transforming the article), 
    then classifies the article with that model and 
    returns list of string name of categories which the article belongs to
    
    params model_path: saved and trained classification model
    params convect_path: saved and filled countvector
    params diff_coef: the difference between the max category result and the others
    """
    
    categ_dict = np.array(['agricult', 'crypto', 'energy', 'metals'])
    model = joblib.load(model_path) 
    convect = joblib.load(convect_path)
    X_test = convect.transform([article])
    
    y_pred = model.predict_proba(X_test).reshape(-1)
    result = categ_dict[y_pred > (y_pred.max() - diff_coef)]
    
    return list(result)


if __name__=='__main__':
	test_data = "An oil production cut of historic proportions was sealed on Easter Sunday (April 12) to help a beleaguered oil and gas industry from hemorrhaging into the ground. It will take 9.7 million barrels per day (bpd) out of the global supply pool to help cope with the economic slump triggered by the coronavirus or Covid-19 global pandemic. Alas, the move hasn't quite calmed the market.But before delving into the reason, here goes the backstory in case you haven't heard - both Russia and Saudi Arabia committed, at least on paper, to reduce 2.5 million bpd from a rehashed headline level of 11 million bpd. Others – both within and and beyond the OPEC+ producersgroup that collapsed so spectacularly on March 6 – pitched in, nudged on by the feverish diplomacy drive undertaken by U.S. President Donald Trump.G20 Energy Ministers committed to another couple of million bpd atop OPEC+'s 9.7 million bpd. Yet for all of that, on Tuesday (April 14), the first full volume oil trading session following the Easter break, the West Texas Intermediate (WTI) May futures contract and the June Brent contract have taken an absolute hammering."
	print(article_classify(X_test_data))    