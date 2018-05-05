/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imgprocessor;

import imgprocessor.indicoWrapper;
import io.indico.api.image.FacialEmotion;
import java.util.Map;

/**
 *
 * @author icarus
 */
public class ImgProcessor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        indicoWrapper ind = new indicoWrapper();
        
        String img = "http://3.bp.blogspot.com/-4OFbq8yO7FM/ThuRjJ5h6lI/AAAAAAAAA7Y/xmMilWJS5Eo/s1600/angry_man_1.jpg";
        ind.parseImage(img);
        System.out.println(ind.getAngry());
    }
    
}
