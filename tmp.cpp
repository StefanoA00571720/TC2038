
//Stefano Herrejon A00571720
using namespace std;


#include <iostream>
#include <vector>
#include <fstream>

vector <int> preproceso(string patron){

    int m = patron.length();

    vector<int> vec(m,0);

    for(int i = 1, j = 0; i < m; i++){
        if(patron[i] == patron[j]){
            vec[i] = j+1;
            j = j+1;
        }else{
            if(j == 0){
                vec[i] = 0;
              
            }else{
                j = vec[i-1];
            }
        }
    }
        
    return vec;
}

vector<int> kmp(string text, string patron, vector<int> vec){
 
    vector<int> lugar;

    int i = 0;
    int j = 0;
    int m = patron.length();
    int n = text.length();

    while(i < n){
        if(text[i] == patron[j]){
            i++;
            j++;
            if(j == m-1){
                lugar.push_back(i-j);
            }
        }else{
            if(j == 0){
                i++;
            }else{
                j = vec[j-1];
            }
        }
    }
    
    return lugar;
}

int main(){

    ifstream archivo("PGD.txt");
    if (!archivo.is_open()) {
        cout << "Error al abrir el archivo." << endl;
    }else{
        cout<<"Todo Bien"<<endl;
    }

    string dracula, linea;

    while(getline(archivo, linea)){
        dracula += linea;
    }

    archivo.close();
    
    //cout<<dracula;

    string pattern = "Dracula";
    //string pattern = "Bram Stoker";
    //strinng pattern = "London";
    //string pattern = "Transylvania";
    //string pattern = "they";

    int n = dracula.length();


    //string pattern = "abcabcdf";
    //string text = "aaaaaabcabcdfaaaaa";

    vector <int> lps = preproceso(pattern);

    vector <int> ans = kmp(dracula, pattern,lps );

    for(int i = 0;i<ans.size();i++){
        cout<<ans[i]<<endl;
        for(int y = 0; y <pattern.size()+50; y++){
            cout<<dracula[ans[i]+y]<<" ";
        }
        cout<<endl;

    }
   

    return 0;
};