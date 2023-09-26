
//Stefano Herrejon A00571720
using namespace std;

#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>


vector<int> funcionZ(string text){
    
    int n = text.length();
    vector<int> vectorZ(n,0);


    for(int i = 1, l = 0, r = 0; i<n;i++){
        if(i <= r){
            vectorZ[i] = min(r-i+1, vectorZ[i-l]);
        }
        while(i + vectorZ[i] < n && text[vectorZ[i]] == text[i+vectorZ[i]]){
            vectorZ[i] = vectorZ[i]+1;
        }
        if(i+vectorZ[i] - 1  > r){
            l = i;
            r = i + vectorZ[i] - 1;
        }
    }

    return vectorZ;
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

    string text = pattern + "$" + dracula;

    int n = dracula.length();
    vector <int> vectorZ = funcionZ(text);

    for(int i = 0;i<n;i++){
        if(vectorZ[i] == pattern.length()){
            for(int y = 0;y<50;y++){
                cout<<text[i+y];
            }
            cout<<endl;
            cout<<endl;
        }
    }

    return 0;
};