// p=>proximo=temp;
//temp->proximo=temp2;
#include <stdlib.h>
#include <iostream>
using namespace std;
int main(void)
{

     struct aluno
    {
        char nome[50];
        float matricula;
        char curso[50];
        struct aluno *proximo;
    };

struct aluno *p;
struct aluno *temp;
struct aluno *temp2;

while (true)
{


p=(struct aluno *)malloc(sizeof(struct aluno));

cout<<"Digite aluno: ";
cin>>p->nome;
cout<<"digite matricula: ";
cin>>p->matricula;
cout<<"digite curso: ";
cin>>p->curso;

cout<<p->nome<<endl;
cout<<p->matricula<<endl;
cout<<p->curso<<endl;

temp=(struct aluno *)malloc(sizeof(struct aluno));
p->proximo=temp;
cout<<"Digite aluno: ";
cin>>p->nome;
cout<<"digite matricula: ";
cin>>p->matricula;
cout<<"digite curso: ";
cin>>p->curso;

cout<<p->nome<<endl;
cout<<p->matricula<<endl;
cout<<p->curso<<endl;

temp2=(struct aluno*)malloc(sizeof(struct aluno));

temp->proximo=temp2;
cout<<"Digite aluno: ";
cin>>p->nome;
cout<<"digite matricula: ";
cin>>p->matricula;
cout<<"digite curso: ";
cin>>p->curso;

cout<<p->nome<<endl; ;
cout<<p->matricula<<endl;
cout<<p->curso<<endl;

cout<<"aceita sair: ";
cin>>res;
if (res=='s'||res=='S'){
p=(struct aluno *)malloc(sizeof(struct aluno));
p=proximo->proximo;
}else break;    

}
   
return 0;}