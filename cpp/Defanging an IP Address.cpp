class Solution {
public:
    string defangIPaddr(string address) {
        string new_address = "";
        for(int i=0;i<address.length();i++){
            if(address[i] == '.'){
                new_address += "[.]";
            }
            else{
                new_address.push_back(address[i]);
            }
        }
        return new_address;
    }
};
