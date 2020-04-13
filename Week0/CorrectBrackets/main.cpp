#include <iostream>
#include <stack>

bool pair(char lhs, char rhs){
    return lhs == '(' && rhs == ')';
}

bool checkBrackets(std::string& exp) {
    std::stack<char> s;
    for(char i: exp){
        if(i == '('){
            s.push(i);
        }else if(i == ')'){
            if(s.empty() || !pair(s.top(), i)){
                return false;
            }else{
                s.pop();
            }
        }
    }
    return s.empty();
}

void enterExpression(){
    std::string exp;
    std::cout << "Input: " << std::endl;
    std::cin >> exp;
    for(char i : exp){
        if(i != '(' && i != ')'){
            throw std::runtime_error("Invalid expression");
        }
    }
    if(checkBrackets(exp)){
        std::cout << "True";
    }else{
        std::cout << "False";
    }

}

int main() {

    enterExpression();
    return 0;
}
