from diff_match_patch import diff_match_patch
import math
dmp = diff_match_patch()

text1="""
#include <bits/stdc++.h>
# using namespace std;
# //hello
# int calc(int a, int b) return a + b;
# int main(){
#    int n , a , b;
#    cin >> n;
#    while(n--){
#         cin >> a >> b;
#         cout << a + b << endl;
#    }
#    return 0;
# }
"""
text2="""
#include <bits/stdc++.h>
# using namespace std;
# //hellola
# int main(){
#    int n , x , y;
#    cin >> n;
#    while(n--){
#         cin >> x >> y;
#         cout << x + y << endl;
#    }
#    return 0;
# }
"""
diff = dmp.diff_main(text1,text2)
idiff = dmp.diff_levenshtein(diff)
per = 100 - (idiff / max(len(text2), len(text1)) * 100)


print(per)
rs = ""
dmp.diff_cleanupSemantic(diff)
rs = ""
flag = 0
for i in diff:
     print(i)



