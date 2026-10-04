def judge(question: str, expects: str, answer: str, results) -> bool:
    '''returns True when the model's answer to a test question
        contains what a correct answer is expected to contain'''
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()