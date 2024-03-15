
def limit(problems):
  if len(problems)<=5:
    return True

def operator(problems):
  for problem in problems:
    parts=problem.split()
    if parts[1]=="//" or parts[1]=="*" or parts[1]=="/":  
      return False
  return True     

def digits(problems):
  for problem in problems:
    parts=problem.split()
    if not (parts[0].isdigit() and parts[2].isdigit()):
      return False
  return True

def len_num(problems):
  for problem in problems:
    parts=problem.split()
    if len(parts[0])>4 or len(parts[2])>4:
      return False
  return True

def formatting(problems, show_answers):
  str1,str2,str3,str4="","","",""

  for problem in problems:

    parts=problem.split()
    operand1=str(parts[0])
    operator=str(parts[1])
    operand2=str(parts[2])

    max_value = max(len(operand1), len(operand2))

    if problem==problems[-1]:
      str1+=f"{operand1:>{max_value+2}}"
      str2+=f"{operator:<{1}}{operand2:>{max_value+1}}"
      str3+="-"*max_value+"--"
    else:
      str1+=f"{operand1:>{max_value+2}}"+ "    "
      str2+=f"{operator:<{1}}{operand2:>{max_value+1}}"+ "    "
      str3+="-"*max_value+"--"+ "    "

    output = str1 + "\n" + str2 + "\n" + str3     

    if show_answers:    
      if operator=="+":
        result=int(operand1)+int(operand2)
      else:
        result=int(operand1)-int(operand2)
      if problem==problems[-1]:
        str4+=f"{result:>{max_value+2}}"
      else:
        str4+=f"{result:>{max_value+2}}"+ "    "
      output += "\n" +str4        

  return output


def arithmetic_arranger(problems, show_answers=False):
  if limit(problems):    
    if operator(problems):
      if digits(problems):
        if len_num(problems):          
            return formatting(problems, show_answers)
        else:
           error=("Error: Numbers cannot be more than four digits.")
      else:
        error=("Error: Numbers must only contain digits.")
    else:
      error=("Error: Operator must be '+' or '-'.") 
  else:
    error=("Error: Too many problems.")
  return error