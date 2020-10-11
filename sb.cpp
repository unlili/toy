#include<vector>
#include<iostream>
#include<string>
#include<set>
using namespace std;
/*
预测S10小组赛的情况
这个程序问题很大,主要是S10的8强比赛是不分小组的,着下面有很多重复的结果,
唯一有价值的就是那个int2singleChar的函数
*/
/*
SN  DWG  GEN  TES   
G2  JDG  FNC  DRX 
*/

vector<int> int2singleChar(unsigned long long a)
{
	/*
	input:12345    output:[1,2,3,4,5]
	input:abcdef    output:[a,b,c,d,e,f]
	*/
	int c = 1;
	long long a_copy = a,a_copy2 = a;
	vector<int> v;

	while ((a/10) > 0 )//获得a是几位数
	{
		++c;
		a /= 10;
	}
	//cout << c << "位数"<<endl;

	for (size_t i = c; i > 0; --i)//5 4 3 2 1 
	{
		unsigned long long w = 1;
		int q = i;
		while (--q)
		{
			w *= 10;
		}// 10000 1000 100 10 1 

		/*
		12345/10000 == 1        
		12345/1000  == 12       %10
		12345/100   == 123      %10  
		12345/10    == 1234     %10 
		12345/1     == 12345    %10
		*/
		a_copy /= w;
		a_copy %= 10;
		
		v.push_back((int)a_copy);

		//cout << "res = " << a_copy << endl;;
		a_copy = a_copy2;
	}
	return v;
}

//测试函数-int2singleChar
void test_int2singleChar()
{
	int t = 1;
	for (size_t i = 1; i < 1000000000000000; i *= 11)
	{
		vector<int> v = int2singleChar(i);
		cout << "第" << t++ << "次:   " <<"i = "<<i<<" ----";
		for (auto i : v)
		{
		    cout<< i << " ";
		}
		cout << endl;
	}
}

bool isCivilWar(unsigned int a)
{
	
	vector<int> v;
	v = int2singleChar(a);
	if (
		(v[0] == 1 && v[4] == 2) ||
		(v[1] == 1 && v[5] == 2) ||
		(v[2] == 1 && v[6] == 2) ||
		(v[3] == 1 && v[7] == 2) ||

		(v[0] == 4 && v[4] == 2) ||
		(v[1] == 4 && v[5] == 2) ||
		(v[2] == 4 && v[6] == 2) ||
		(v[3] == 4 && v[7] == 2)
		)
	{
		return true;
	}
	return false;
}

//所有结果
void printAllRes(vector<unsigned int> v1, vector<string> first,vector<string> second)
{
	vector<int> v;
	cout << v1.size() << endl;
	for (size_t i = 0; i < v1.size();++i)
	{
		v = int2singleChar(v1.at(i));

		for (auto & wq : v)
		{
			wq -= 1;
		}
		cout << "第" << i+1<<"种"<<string(20, '-') << endl;

		cout << first.at(v[0]) << "-" << second.at(v[4]) << "   " << first.at(v[1]) << "-" << second.at(v[5]) << "   " << first.at(v[2]) << "-" << second.at(v[6]) << "   " << first.at(v[3]) << "-" << second.at(v[7]) << endl;


		cout << string(20, '-') << endl;
	}

}

//没有内战
void printAllRes_no(vector<unsigned int> v1, vector<string> first, vector<string> second)
{
	vector<int> v;
	//没有内战的结果
	int cnp = 0;
	for (size_t i = 0; i < v1.size();++i)
	{
		if (isCivilWar(v1.at(i))) continue;
		v = int2singleChar(v1.at(i));

		for (auto & wq : v)
		{
			wq -= 1;
		}
		cout << "第" << ++cnp<<"种"<<string(20, '-') << endl;

		cout << first.at(v[0]) <<"-"<< second.at(v[4])  << "   "<< first.at(v[1]) <<"-" << second.at(v[5])<<"   "<< first.at(v[2]) << "-" << second.at(v[6]) << "   "<< first.at(v[3]) << "-" << second.at(v[7]) << endl;

		cout << string(20, '-') << endl;
	}

}

//只有内战
void printAllRes_yes(vector<unsigned int> v1, vector<string> first, vector<string> second)
{
	vector<int> v;
	//只有内战的结果
	int cnp = 0;
	for (size_t i = 0; i < v1.size();++i)
	{
		if (isCivilWar(v1.at(i)))
		{ 
		v = int2singleChar(v1.at(i));

		for (auto & wq : v)
		{
			wq -= 1;
		}
		cout << "第" << ++cnp<<"种"<<string(20, '-') << endl;

		cout << first.at(v[0]) <<"-"<< second.at(v[4])  << "   "<< first.at(v[1]) <<"-" << second.at(v[5])<<"   "<< first.at(v[2]) << "-" << second.at(v[6]) << "   "<< first.at(v[3]) << "-" << second.at(v[7]) << endl;

		cout << string(20, '-') << endl;
		}
	}

}


int main()
{
	vector<string> first;
	vector<string> second;

	first.push_back(" SN");
	first.push_back("DWG");
	first.push_back("GEN");
	first.push_back("TES");

	second.push_back(" G2");
	second.push_back("JDG");
	second.push_back("FNC");
	second.push_back("DRX");

	vector<int> v;
	vector<int> v_single;
	size_t count=0;

	for (size_t a = 1; a <= 4; ++a)
	{
		for (size_t b = 1; b <= 4; ++b)
		{
			for (size_t c = 1; c <= 4; ++c)
			{
				for (size_t d = 1; d <= 4; ++d)
				{
					if (a != b && a != c && a != d && b!=d && c!= d && c !=b)
					{
						v.push_back(a*1000+b*100+c*10+d);
						++count;
					}
				}
			}
		}
	}
	
	vector<unsigned int> res_all;

	for (auto i : v)
	{
		for (auto j : v)
		{
			res_all.push_back(i*10000+j);
		}
	}

	vector<unsigned int> res_all_final;


	vector<int> temp;
	for (auto i : res_all)
	{
		//1234 1234
		//0123 4567
		temp = int2singleChar(i);

		if (temp[0] != temp[4] && temp[1] != temp[5] && temp[2] != temp[6] && temp[3] != temp[7])
		{
			res_all_final.push_back(i);
		}
	}

	printAllRes_no(res_all_final,first,second);//打印所有比赛结果

	//cout << isCivilWar(12342341) << endl;
	return 0;
}
