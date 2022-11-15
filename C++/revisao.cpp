#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;
typedef struct aluno{
char nome[50],curso[50];
int matricula;
struct aluno*proximo,*anterior;
}temp;

bool fim (char *nome);

int main(){
    temp*entrada;
    temp*regist;
    temp*final;

    entrada = (temp*)malloc(sizeof(temp));
    regist = entrada;
    regist->anterior=NULL;

    while(1){
        cout<<"\n DIGITE O NOME: ";
        cin>>regist->nome;
        if(fim(regist->nome))break;
        cout <<"\n DIGITE A MATRICULA ";
        cin>>regist->matricula;
        cout<<"\n DIGITE O CURSO: ";
        cin>>regist->curso;

        regist->proximo=(temp*)malloc(sizeof(temp));
        
        regist->anterior=final;
        final=regist;

        regist=regist->proximo;
    }
    regist=final;

    while(1){
        if (regist==NULL)break;
        cout<<"\n Nome: "<<regist->nome;
        cout<<"\n Curso: "<<regist->curso;
        cout<<"\n matricula: "<<regist->matricula;
        }
        regist=regist->anterior;
}
    bool fim(char*nome){
    if(strcmp(nome , "fim")==0)return true;
    return false;
    }

