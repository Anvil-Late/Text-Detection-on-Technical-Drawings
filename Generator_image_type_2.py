# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont
import numpy as np
import glob
import random
import cv2
import os
import json
import xml.etree.ElementTree as xml





dir_path = r"C:\Users\Alten Canada\Documents\GitHub\Text-Detection-on-Technical-Drawings\src_img\*.png"
Images = glob.glob(dir_path)

print(len(Images),'elements were found and loaded!')

summary_dict = {}






def image_type_2(num_imgs,annotation=True):
    """Generates defined number of image type 2 images in .jpg format and PASCAL VOC annotation file in .xml format.
    
    Args:
        num_imgs (int): Amount of images to generate
        annotation (bool): Wether an annotiation file should be generated
        
    """
       
    
    k=0
    
    while (k<num_imgs):
        
        masse_hor=[]
        durch_hor=[]
        masse_ver=[]
        durch_ver=[]
        
        
        # generation of blank image
        
        img_x=random.randint(1200,1500)
        img_y=int(img_x/(2**(0.5)))
        image=Image.new('RGBA', (img_x, int(img_y)), (255,255,255))
        
        
        # number of elements
        num_elements = random.randint(130,150)
        
        
        # creation of background 
        i=0
                
        while i < num_elements:
           
                
            element_choice = random.randint(0,len(Images)-1)
            element_location = (random.randint(0,img_x),random.randint(0,img_y))
            element = Image.open(Images[element_choice]) 
        
            image.paste(element, element_location)
        
            i+=1

        text_dict = {}
        
        # horizontal dimensions
        text_dict["l"] = {}

        j=0
        while j < 10:

            font_size=16
            
            
            threshold = random.uniform(0,1)
            
            if threshold > 0.75:
                text=random.randint(0,20)
            else:
                text=round(random.uniform(1,200), 1)
                text_int = text.is_integer()

                if text_int == True:
                     
                     text=int(text)

            text_dict["l"][j] = text
            
            
            text=str(text)
                                   
            text = text.replace('.',',')
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            font_glossar_choice = 'arial.ttf'
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text) 
            
            image2=Image.new('RGBA', (width, height), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            image.paste(image2, txt_pt , image2)
            
            if font_glossar_choice=='isocpeui.ttf':
                min_x = txt_pt[0]
                min_y = txt_pt[1]-3
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1+3 
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1
            
            
            b_box = (min_x, min_y, max_x, max_y)
            masse_hor.append(b_box)
                                            
            
            j+=1
        
        
        
        
        
        

        
        # horizontal diameter
        
        m=0
        text_dict["n"] = {}
        while m < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            text_dict["n"][m] = text

            text_int = text.is_integer()
        
            if text_int == True:
                
                text=int(text)
            
            
            text=str(text)
                        
                        
            text = text.replace('.',',')
            
            spacing_choice=['',' ','  ']
            spacing=random.choice(spacing_choice)
            
            text = '\u2300' + spacing + text
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            font_glossar_choice = 'arial.ttf'
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text) 
            
            image2=Image.new('RGBA', (width, height), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                min_x = txt_pt[0]
                min_y = txt_pt[1]-3
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1+3 
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1
            
            
            b_box = (min_x, min_y, max_x, max_y)
            durch_hor.append(b_box)
            
                                                            
            m+=1
        
        
        
        
 
       
        # vertical dimension
        text_dict["p"] = {}
        o=0
        while o < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            text_dict["p"][o] = text
            text_int = text.is_integer()
        
            if text_int == True:
                
                text=int(text)
            
                                                            
            text = str(text)
            
            spacing_choice=['',' ','  ']
            
            spacing=random.choice(spacing_choice)
            
            text = '\u2300' + spacing + text
            text = text.replace('.',',')
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']

            font_glossar_choice=random.choice(font_glossar)
            font_glossar_choice = 'arial.ttf'
            
            unicode_text=text.encode('utf-8')
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
            
            
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            image2=image2.rotate(90, expand=1)
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-70))
            
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                
                min_x = txt_pt[0]-3
                min_y = txt_pt[1]+2
                max_x = txt_pt[0]+height+1+3
                max_y = txt_pt[1]+width-2
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]-2
                max_x = txt_pt[0]+height+1
                max_y = txt_pt[1]+width
            
            
            
            
    
            
            b_box = (min_x, min_y, max_x, max_y)
            durch_ver.append(b_box)
        
            o+=1
        
        
        
        
        
        # vertical diameter
        text_dict["r"] = {}
        q=0
        while q < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            text_int = text.is_integer()
            text_dict["r"][q] = text

            if text_int == True:
                
                text=int(text)
            
           
            text = str(text)
            
            
            text = text.replace('.',',')
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            
            
            unicode_text=text.encode('utf-8')
            font_glossar_choice = 'arial.ttf'
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
            
            
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            image2=image2.rotate(90, expand=1)
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-70))
            
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                
                min_x = txt_pt[0]-3
                min_y = txt_pt[1]+2
                max_x = txt_pt[0]+height+1+3
                max_y = txt_pt[1]+width-2
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]-2
                max_x = txt_pt[0]+height+1
                max_y = txt_pt[1]+width
            
            
            
            
    
            
            b_box = (min_x, min_y, max_x, max_y)
            masse_ver.append(b_box)
        
            q+=1
        
        
                                            
        
        img=np.array(image)
        cv2.imwrite('./gen_img/00%s.jpg'%k, img)
            
            
        
            
        summary_dict["00%s.jpg"%k] = {}
        if annotation==True:    
            
        
            xml_doc = xml.Element("annotation")
            
            folder=xml.SubElement(xml_doc,"folder")
            filename=xml.SubElement(xml_doc,"filename")
            path=xml.SubElement(xml_doc,"path")
            source=xml.SubElement(xml_doc,"source")
            database=xml.SubElement(source,"database")
            size=xml.SubElement(xml_doc,"size")
            width=xml.SubElement(size,"width")
            height=xml.SubElement(size,"height")
            depth=xml.SubElement(size,"depth")
            segment=xml.SubElement(xml_doc,"segmented")
                    
                              
            
            folder.text="Test"
            filename.text=("00%s.jpg"%k)
            summary_dict["00%s.jpg"%k]["filename"] = "00%s.jpg"%k
            path.text="Unknown"
            database.text="Unknown"
            width.text=str(img_x)
            summary_dict["00%s.jpg" % k]["width"] = str(img_x)
            height.text=str(img_y)
            summary_dict["00%s.jpg" % k]["height"] = str(img_y)
                    
            #depth grayscale=0, color=3
            depth.text="3"
            segment.text="0"
                    
            
            l=0
                    
            while l < len(masse_hor):
                item_descr = {}
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_hor'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(masse_hor[l][0]))
                ymin.text=str(int(masse_hor[l][1]-2))
                xmax.text=str(int(masse_hor[l][2]))
                ymax.text=str(int(masse_hor[l][3]+2))
                item_descr["text"] = text_dict["l"][l]
                item_descr["xmin"] = int(masse_hor[l][0])
                item_descr["ymin"] = int(masse_hor[l][1]-2)
                item_descr["xmax"] = int(masse_hor[l][2])
                item_descr["ymax"] = int(masse_hor[l][3]+2)

                summary_dict["00%s.jpg" % k][f"item_l_{l}"] = item_descr
                l+=1


            
            n=0
                    
            while n < len(durch_hor):
                item_descr = {}
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_hor'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(durch_hor[n][0]))
                ymin.text=str(int(durch_hor[n][1]-2))
                xmax.text=str(int(durch_hor[n][2]))
                ymax.text=str(int(durch_hor[n][3]+2))
                item_descr["text"] = text_dict["n"][n]
                item_descr["xmin"] = int(durch_hor[n][0])
                item_descr["ymin"] = int(durch_hor[n][1] - 2)
                item_descr["xmax"] = int(durch_hor[n][2])
                item_descr["ymax"] = int(durch_hor[n][3] + 2)

                summary_dict["00%s.jpg" % k][f"item_n_{n}"] = item_descr
            
                n+=1
                    
            p=0
                    
            while p < len(masse_ver):
                item_descr = {}
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_ver'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(masse_ver[p][0]))
                ymin.text=str(int(masse_ver[p][1]-2))
                xmax.text=str(int(masse_ver[p][2]))
                ymax.text=str(int(masse_ver[p][3]+2))
                item_descr["text"] = text_dict["p"][p]
                item_descr["xmin"] = int(masse_ver[p][0])
                item_descr["ymin"] = int(masse_ver[p][1] - 2)
                item_descr["xmax"] = int(masse_ver[p][2])
                item_descr["ymax"] = int(masse_ver[p][3] + 2)

                summary_dict["00%s.jpg" % k][f"item_p_{p}"] = item_descr
            
                p+=1
            
            r=0
                    
            while r < len(durch_ver):
                item_descr = {}
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_ver'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(durch_ver[r][0]))
                ymin.text=str(int(durch_ver[r][1]-2))
                xmax.text=str(int(durch_ver[r][2]))
                ymax.text=str(int(durch_ver[r][3]+2))
                item_descr["text"] = text_dict["r"][r]
                item_descr["xmin"] = int(durch_ver[r][0])
                item_descr["ymin"] = int(durch_ver[r][1] - 2)
                item_descr["xmax"] = int(durch_ver[r][2])
                item_descr["ymax"] = int(durch_ver[r][3] + 2)

                summary_dict["00%s.jpg" % k][f"item_r_{r}"] = item_descr
            
                r+=1        
            
            
            
            
            
            
            def prettify(element, intend=' '):
                queue = [(0,element)]
                while queue:
                    level, element =queue.pop(0)
                    children = [(level + 1, child)for child in list(element)]
                    if children:
                        element.text = '\n' + intend * (level+1)
                        if queue:
                            element.tail = '\n' + intend * queue[0][0]
                        else:
                            element.tail = '\n' + intend * (level-1)
                            queue[0:0] = children
                    
            
            prettify(xml_doc)
                          
                        
            tree = xml.ElementTree(xml_doc)
            tree.write('./gen_img/00%s.xml'%k)

            with open('./gen_img/00%s.json'%k, 'w') as f:
                json.dump(summary_dict, f)
        
        
        
        k+=1


#with open(r"C:\Users\Alten Canada\Documents\GitHub\Text-Detection-on-Technical-Drawings\gen_img\000.json", 'r') as f:
#    summary_dict = json.load(f)
    

image_type_2(5)    
    
    
    
    
    
    
   
