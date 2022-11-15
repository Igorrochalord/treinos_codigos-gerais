#include "iostream"
#include <cstdlib>
using namespace std;
int main (void)
{
struct aluno
{
    char nome [50];
    float matricula;
    char curso [50];
    struct aluno*p;
};

    struct aluno *p;
    int i;
    for( i= 0; i<1; i++) {
        p = (struct aluno*)malloc(sizeof(struct aluno));
        cout<<"Digite o seu nome: ";
        cin>>p->nome;
    }

return 0;}