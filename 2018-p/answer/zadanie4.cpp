#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

void generuj_plik(int ile, int zakres)
{
    srand(time(NULL));
    int n;
    ofstream wy("ciagi.txt");
    wy<<ile<<endl;
    for (int i=0; i<ile-1; ++i)
    {
        n=rand()%zakres+1;
        wy<<n<<" ";
        for (int j=0; j<n-1; ++j) wy<<rand()%(2*zakres+1)-zakres<<" ";
        wy<<rand()%(2*zakres+1)-zakres;
        wy<<endl;
    }
        n=rand()%zakres+1;
        wy<<n<<" ";
        for (int j=0; j<n-1; ++j) wy<<rand()%(2*zakres+1)-zakres<<" ";
        wy<<rand()%(2*zakres+1)-zakres;
    wy.close();
}

void czytaj(int n, int *t)
{
    for (int i=0; i<n; ++i)cin>>t[i];
}
void wypisz(int n, int *t)
{
    for (int i=0; i<n; ++i) cout<<t[i]<<" ";
    cout<<endl;
}


void ciag(int n, int *t, int &najdluzszy, vector<int> &wynik)
{
    int d[n],nr[n];
    d[0]=1;
    nr[0]=0;
    for (int i=1;i<n; ++i)
    {
        d[i]=1;
        nr[i]=0;
        for (int j=0; j<i; ++j)
        {
            if (t[j]<t[i])
                if (d[i]<d[j]+1)
                {
                    d[i]=d[j]+1;
                    nr[i]=j;
                }
                else
                d[i]=max(d[i], d[j]+1);
        }
    }
  wypisz(n,d);
  wypisz(n,nr);
  najdluzszy=d[0];
  int miejsce=0;
  for (int i=1; i<n; ++i)
    {
        if (najdluzszy<d[i])
        {
            najdluzszy=d[i];
            miejsce=i;
        }
    }
  wynik.push_back(t[miejsce]);
  for (int i=miejsce-1; i>=0;--i)
  {
     if (d[miejsce]==d[i]+1)
     {
         wynik.push_back(t[i]);
         miejsce=i;
     }
  }

}
/* Przykladowe dane:
  t[i]  7 8 3 1 3 5 4 5 7 6
  d[i]  1 2 1 1 2 3 3 4 5 5
  nr[i] 0 0 0 0 3 4 4 6 7 7
*/
int main()
{
    //generuj_plik(100,50);
    ifstream we("ciagi.txt");
    ofstream wy("podciagi.txt");
    int ile_ciagow, dlugosc,maks;
    we>>ile_ciagow;
    for (int i=0; i<ile_ciagow;++i)
    {
        we>>dlugosc;
        int liczby[dlugosc];
        cout<<endl<<"dlugosc "<<dlugosc<<endl;
        for (int j=0; j<dlugosc; ++j) we>>liczby[j];
        wypisz(dlugosc,liczby);
        vector<int> elementy_maks;
        ciag(dlugosc, liczby, maks, elementy_maks);
        cout<<"Dlugosc najdluzszego podciagu="<<maks<<endl;
        wy<<maks<<endl;
        cout<<"Elementy przykladowego najdluzszego podciagu:"<<endl;
        for (int i=elementy_maks.size()-1; i>=0; --i) cout<<elementy_maks[i]<<" ";
    }
    we.close();
    wy.close();
    return 0;
}
