//Stefano Herrejon A00571720

using namespace std;

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

string manacher(string dracula){

    //cout<<"llego a la funcion"<<endl;

    //Centro del palodromo más a la derecha, la derecha del palindromo más a la derecha, y a la izquierda
    int C = 0, L = 0, R = 0;

    //Valores para calcuar si hay palindrome
    int rl = 1;

    //m = longitud del palindromo más grande, pl = indice de la mitad del palidromo en T
    int m = 0, pl = 0;

    int j = 0;

    string T = "|", palindromo = "";

    for(int i = 0; i<dracula.length();i++){
        T = T + dracula[i] + "|";
    }

    int N = T.length();

    vector<int> palindromes(N,0);

    for(int i = 0;i < N;i++){

        if(i < R){
            j = 2 * C - i;
            palindromes[i] = min(R - i, palindromes[j]);
            
        }

        rl = palindromes[i]+1;

        while(tolower(T[i-rl]) == tolower(T[i+rl]) && i-rl>=0 && i+rl<N ){
            //if(T[i-rl]!='|')
                //cout<<T[i-rl]<<"-"<<T[i+rl]<<endl;
            palindromes[i]++;
            rl++;
        }

        if(palindromes[i] > m){
            pl = i;
            m = palindromes[i];
        }

        if(i + palindromes[i] > R){
            R = i + palindromes[i];
            C = i;
        }   
    }

    string ans = "";
    /*
    for(int i = 0;i<N;i++){
       cout<<palindromes[i]<<" ";
    }
    */
    
    for(int i = 0;i<m*2+1;i++){
        if ( T[pl-m+i] != '|')
            ans += T[pl-m+i];
    }

    //cout<<"m:"<<m<<" pl "<<pl<<" Palabra : "<<T[pl]<<endl;
    
    return ans;
}

int main() {
    //Leer archivo

    ifstream archivo("PGD.txt");
    if (!archivo.is_open()) {
        cout << "Error al abrir el archivo." <<endl;
        return 1;
    }

    string dracula, linea;

    while (getline(archivo, linea)) {
        istringstream iss(linea);
        string palabra;
        while (iss >> palabra) {
            dracula = dracula + palabra;
        }
    }

    archivo.close();

    //cout<<dracula<<endl;

    cout<<manacher(dracula)<<endl;

    return 0;
}
