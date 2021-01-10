func countSubstrings(s string) int {
    n:=len(s)
    count:=0
    dp:=make([][]int,n)
    for k:=0;k<n;k++{
        dp[k]=make([]int,n)
    }
    for j:=0;j<n;j++{
        for i:=0;i<=j;i++{
            if string(s[i])==string(s[j]) && (j-i<2 || dp[i+1][j-1]==1){
                dp[i][j]=1
                count++
            }
        }
    }
    return count
}
