//Equiupo 2
//Actividad integradora

/*
Diego Sebastián García Cabrera A01634071 
Stefano Herrejon Antuñano A00571720
Edgar Fabían Lioner Rocha A01633776
Juan Pablo Zambrano Barajas A01636420
*/

using namespace std;

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cctype>

//Funcion para leer los archivos
string leerarchivo(string nombre){

    string texto = "";
    string linea;

    ifstream archivo(nombre);
    if (!archivo.is_open()) {
        cout << "Error al abrir el archivo." <<endl;
        return "error";
    }

    while (getline(archivo, linea)) {
        istringstream iss(linea);
        string palabra;
        while (iss >> palabra) {
            texto = texto + palabra;
        }
    }

    archivo.close(); 
    return texto;
}

//Funcion Z
vector<int> funcionZ(string text, string pattern){

    text = pattern + "$" + text;
    
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

    for(int i = 0;i<n;i++){
        if(vectorZ[i] == pattern.length()){
            cout<<"Se encontro el patron"<<endl;
            for(int y = 0;y<pattern.length();y++){
                cout<<text[i+y];
            }
            cout<<endl;
            cout<<endl;
        }
    }

    return vectorZ;
}

//Llamar a la funcion Z
void llamarFZ(string texto, string patternA, string patternB, string patternC){
    
    cout<<"mcode1 "<<endl;
    funcionZ(texto, patternA);

    cout<<"mcode2"<<endl;
    funcionZ(texto,patternB);

    cout<<"mcode3"<<endl;
    funcionZ(texto,patternC);

}

//KMP
//Preproceso del patron
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

//Funcino kmp y cout
void kmp(string text, string patron){
 
    vector<int> lugar;
    vector<int> vec = preproceso(patron);

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

    for(int i = 0;i<lugar.size();i++){
        //cout<<lugar[i]<<endl;
        for(int y = 0; y <patron.size(); y++){
            cout<<text[lugar[i]+y];
        }
        cout<<endl;
    }
    cout<<endl;

    
}

//Llamar a la función kmp
void llamarKMP(string texto, string patternA, string patternB, string patternC){
    cout<<"mcode1"<<endl;
    kmp(texto, patternA);

    cout<<"mcode2"<<endl;
    kmp(texto,patternB);

    cout<<"mcode3"<<endl;
    kmp(texto,patternC);
}

//Manacher

void manacher(string texto){

    //cout<<"llego a la funcion"<<endl;

    //Centro del palodromo más a la derecha, la derecha del palindromo más a la derecha, y a la izquierda
    int C = 0, L = 0, R = 0;

    //Valores para calcuar si hay palindrome
    int rl = 1;

    //m = longitud del palindromo más grande, pl = indice de la mitad del palidromo en T
    int m = 0, pl = 0;

    int j = 0;

    string T = "|", palindromo = "";

    for(int i = 0; i<texto.length();i++){
        T = T + texto[i] + "|";
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
    
    cout<<"Longitud del palindromo : "<<m<<endl;

    for(int i = 0;i<m*2+1;i++){
        if ( T[pl-m+i] != '|')
            cout<< T[pl-m+i];
    }

    cout<<endl;
    cout<<endl;

}


//Substring mas grande extre 2 textos
void substring(string texto, string linea){

    int m = texto.length();//Filas
    int n = linea.length();//Columnas

    int ans = 0;
    int posT = 0;

    vector<vector<int>> matriz(m,vector<int>(n, 0));

    for(int i = 0;i<m;i++){


        for(int j = 0; j<n;j++){

            if(tolower(texto[i]) == tolower(linea[j])){

                if(i == 0 || j == 0){

                    matriz[i][j] = 1;

                }else{

                    matriz[i][j] = matriz[i-1][j-1]+1;

                    if(matriz[i][j]>ans){
                        ans = matriz[i][j];
                        posT = i;
                    }

                }
            }
        }
    }

    cout<<"Substring más grande : "<<ans<<endl;
    for(int i = 1;i<=ans;i++){
        cout<<texto[posT-ans+i];
    }
    cout<<endl;
    cout<<endl;
}

int main() {
    //Leer archivo

    string textoA = leerarchivo("transmission1.txt");
    string textoB = leerarchivo("transmission2.txt");

    string malwareA = leerarchivo("mcode1.txt");
    string malwareB = leerarchivo("mcode2.txt");
    string malwareC = leerarchivo("mcode3.txt");

    /*
    cout<<textoA<<endl;
    cout<<textoB<<endl;
    cout<<malwareA<<endl;
    cout<<malwareB<<endl;
    cout<<malwareC<<endl;
    */
   
  
   cout<<"Usando la funcionZ se encontro en la transmission1: "<<endl;
   llamarFZ(textoA,malwareA,malwareB,malwareC);

    cout<<"Usando la funcionZ se encontro en el transmission2:"<<endl;
    llamarFZ(textoB,malwareA,malwareB,malwareC);
    

    cout<<"Usando la KMP se encontro en el transmission1:"<<endl;
    llamarKMP(textoA,malwareA,malwareB,malwareC);

    
    cout<<"Usando la KMP se encontro en el transmission2:"<<endl;
    llamarKMP(textoB,malwareA,malwareB,malwareC);
    

   cout<<"Usando la manacher se encontro el palindrome en transmission1"<<endl;
    manacher(textoA);

    cout<<"Usando la manacher se encontro el palindrome en transmission2"<<endl;
    manacher(textoB);

    cout<<"Substring más grande entre transmission1 y transmission2"<<endl;
    substring(textoA, textoB);

    cout<<"Substring más grande entre mcode1 y mcode2 "<<endl;
    substring(malwareA, malwareB);

    cout<<"Substring más grande entre mcode1 y mcode3 "<<endl;
    substring(malwareA, malwareC);

    cout<<"Substring más grande entre mcode2 y mcode3 "<<endl;
    substring(malwareB, malwareC);

    return 0;
}
