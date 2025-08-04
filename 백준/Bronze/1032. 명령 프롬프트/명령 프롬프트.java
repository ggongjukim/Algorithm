import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];  //파일 이름 저장하는 배열
        
        char[] pattern = br.readLine().toCharArray();

        for(int i = 0; i < n-1 ;i++){
            char[] tmpFileName = br.readLine().toCharArray();

            for(int j = 0 ; j <  pattern.length; j++){
                if( pattern[j] != tmpFileName[j] )
                {
                    pattern[j] = '?';
                }
            }
        }
        System.out.println(pattern);
    }
}