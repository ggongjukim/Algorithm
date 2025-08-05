import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // int N = Integer.parseInt(br.readLine());
        // StringBuilder outArr = new StringBuilder(); // 
        String s;
        while((s = br.readLine()) != null ){
            int a = 0;
            int b = 0;
            int c = 0;
            int d = 0;
            char[] inputArr = s.toCharArray();
            
            for(int j = 0 ; j <  inputArr.length; j++){
                // 소문자
                if( Character.isLowerCase(inputArr[j])){
                     a += 1;
                }
                // 대문자
                else if(Character.isUpperCase(inputArr[j])){
                    b += 1;
                }
                
                // 숫자
                else if(Character.isDigit(inputArr[j])){
                    c += 1;
                }
                
                // 공백
                else if(inputArr[j] == ' '){
                    d +=1;
                }
            }
            System.out.println(a +  " " + b +  " " + c + " " + d );
            // outArr.append(tmp)
        }
        // System.out.println(pattern);
    }
}