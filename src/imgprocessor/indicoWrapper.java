/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imgprocessor;

import io.indico.Indico;
import io.indico.api.image.FacialEmotion;
import io.indico.api.results.IndicoResult;
import java.awt.Rectangle;
import javax.imageio.ImageIO;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

/**
 *
 * @author icarus
 */
public class indicoWrapper {
    Indico ind;
    Map<FacialEmotion,Double> workingInput;
    private double sad, neutral, angry, surprise, fear, happy;
    
    indicoWrapper(){
        try{
            ind = new Indico("23953ee91667f678a12e566e766b6f56");
        }catch (Exception e){
            System.out.println("--Exception--");
            System.out.println(e);
        }
    }
    
    public void parseImage(String file){
        IndicoResult response;
        //List<String>> csvList = new ArrList<String>>();
        Map<FacialEmotion,Double> output = null;
       
        try{
            response = ind.fer.predict(file);
            output = response.getFer();
        }catch (Exception e){
            System.out.println("--Exception--");
            System.out.println(e);
        }   
        workingInput = output;
        
        process();
    }
    
    private void process(){
        for(FacialEmotion key: workingInput.keySet()){
            if (key == FacialEmotion.Sad){
                sad = workingInput.get(key);
            }else if (key == FacialEmotion.Neutral){
                neutral = workingInput.get(key);
            }else if (key == FacialEmotion.Angry){
                angry = workingInput.get(key);
            }else if (key == FacialEmotion.Surprise){
                surprise = workingInput.get(key);
            }else if (key == FacialEmotion.Fear){
                fear = workingInput.get(key);
            }else if (key == FacialEmotion.Happy){
                happy = workingInput.get(key);
            }
        }
    }
    public double getSad(){
        return sad;
    }
    public double getNeutral(){
        
        return neutral;
    }
    public double getAngry(){
        return angry;
    }
    public double getSurprise(){
        return surprise;
    }
    public double getFear(){
        return fear;
    }
    public double getHappy(){
        return happy;
    }
    
}
