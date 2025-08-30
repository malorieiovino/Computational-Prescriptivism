from pdci import analyze_pair

def test_loss_case():
    src = "I think it might have been Tuesday, I'm not sure, um, around 9 in the evening."
    summ = "It was Tuesday at 9 PM."
    result = analyze_pair(src, summ)
    print("LOSS CASE:", result)
    assert 0 <= result["PDCI"] <= 1

def test_hallucination_case():
    src = "He said it was about 10, maybe later, but I can't remember exactly."
    summ = "He said it was definitely 10 o'clock sharp without doubt."
    result = analyze_pair(src, summ)
    print("HALLUCINATION CASE:", result)
    assert result["hallucination_rate"] >= 0
    assert 0 <= result["PDCI"] <= 1

def test_certainty_inflation_case():
    src = "Perhaps Wednesday or Thursday, I believe. Uh, not totally sure."
    summ = "It was certainly Wednesday."
    result = analyze_pair(src, summ)
    print("CERTAINTY INFLATION CASE:", result)
    assert result["CII"] > 0
    assert 0 <= result["PDCI"] <= 1

def test_balanced_case():
    src = "I suppose it could have been Friday, unless it was Thursday night."
    summ = "It was Friday."
    result = analyze_pair(src, summ)
    print("BALANCED CASE:", result)
    assert "loss_rate" in result
    assert "hallucination_rate" in result
    assert "PDCI" in result
def test_pdci_score_range():
    result = analyze_pair("I think it might rain tomorrow.", "It will rain tomorrow.")
    assert 0 <= result["PDCI"] <= 1
