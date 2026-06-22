#include <bits/stdc++.h>
#include <math.h>
#include <cmath>
using namespace std;


int main(){
    double y=-10,w;
    

    vector<vector<double>> v;

    //y=-0.1(w+10)^2 + 10
    for(int i=0 ; i <11 ; i++,y++){

        // cout<<"The coordinates for point"<<i<<endl;

    
        // w = -sqrt((y-20)*(-225)/20);
        // double x = (35+w)/(sqrt(2));
        // double z = (35-w)/(sqrt(2));
        
        // cout<<x << endl;
        // cout<<z << endl;
        
        // cout<<"------"<<endl; 
        
        w = -sqrt((y)*(-25)/10)+(15);
        double x = (w)/(sqrt(2));
        double z = (w)/(sqrt(2));

        double x_trans=-x*(sqrt(3)/2)+(z/2)+20*cos(30*M_PI/180);
        double z_trans=-(x/2)-(z)*(sqrt(3)/2)+20*sin(30*M_PI/180);
        // cout << w << endl;
        //  cout << -x/2 << endl;
        //  cout << (z)*(-sqrt(3)/2) << endl;
        //  cout << 15*sqrt(3)*cos(15*M_PI/180) << endl;
        //  break;
        
        cout<<x_trans << endl;
        cout<<z_trans << endl;
            vector<double> temp;
            temp.push_back(x_trans);
            temp.push_back(y);
            temp.push_back(z_trans);
            v.push_back(temp);
            

    }  
    y--;
    y--;
    for(int i=0;i<11;i++,y--){
          
        cout <<"The coordinates for point"<<i<<endl;
//  break;
    
        w = +sqrt((y)*(-25)/10)+15;
         double x = (w)/(sqrt(2));
        double z = (w)/(sqrt(2));
        double x_trans=-x*(sqrt(3)/2)+(z/2)+20*cos(30*M_PI/180);
        double z_trans=-(x/2)-(z)*(sqrt(3)/2)+20*sin(30*M_PI/180);
            //  cout << w << endl;
            //   cout << -x/2 << endl;
            //   cout << (z)*(-sqrt(3)/2) << endl;
            //   cout << 15*sqrt(3)*cos(15*M_PI/180) << endl;

        cout<<x_trans << endl;
        cout<<z_trans << endl;
        vector<double> temp;
            temp.push_back(x_trans);
            temp.push_back(y);
            temp.push_back(z_trans);
            v.push_back(temp);
    }
    // if(y==0){
    //     w=0;
    //     double x = (40+w)/(sqrt(2));
    //     double z = (40-w)/(sqrt(2));
    
    //     cout<<x << endl;
    //     cout<<z << endl;
    // }
    cout << endl;
    cout << '[' ;
   for(int i=0;i<21;i++){
    cout << '[' ;
    for(int j=0;j<3;j++){
        if(j!=2){
            cout << v[i][j] << " " << ',';
        }
        else{
            cout << v[i][j];
        }
    }cout << "]," << endl;
   }cout << ']' ;

    return 0;

    

} left back