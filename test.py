from bardapi import Bard
import os

#替换为之前获得的 __Secure-1PSID 
os.environ['_BARD_API_KEY']="YwiBWxpo7V2wDmScRWtZZ_rjDuvLczxZwO2wtcZkgTyFyk3N7SYkdKIa5bUJC1ajw4I6-Q."

input_text = "bard能做些什么?"
print(Bard().get_answer(input_text)['content'])