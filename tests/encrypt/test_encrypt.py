import pytest
from challenges.challenge_encrypt_message import encrypt_message

# keys
key = 3
other_key = 7
wrong_key = 'a'


# messages
message = "valete"
wrong_message = 848

# casos de erro
error1 = "tipo inválido para key"
error2 = "tipo inválido para message"

# resposta
answer = "lav_ete"
invert_answer = "etelav"


def test_encrypt_message():
    with pytest.raises(TypeError, match=error1):
        encrypt_message(message, wrong_key)
    with pytest.raises(TypeError, match=error2):
        encrypt_message(wrong_message, key)
        
    assert encrypt_message(message, key) == answer
    assert encrypt_message(message, other_key) == invert_answer
