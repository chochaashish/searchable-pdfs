# searchable-pdfs
make non-searchable pdfs searchable using tesseract-ocr engine and magick 

                    ====== Installation ======
* Install all libraries from 'lib' folder
* Set Environment variable: PATH: 'path where tesseract is installed'
                            <p>  TESSDATA_PREFIX: 'path where tesseract is installed/ folder "tessdata"/' </p>
                             </br> 

                    ====== Configuration ======
* Change root folder where you want to search for pdfs:
        open file > config.py
                        > Change path of 'ROOT_FOLDER'
* Maintain password protected files with "assets/password_data.csv"
        our script replace original(password protected) pdf with same name pdf(without password).
        format of content:
        <p>      path of file1, password1 </p>
              <p> path of file2, password2 </p>
              ..
              ..
              ..
* You can check logs of running script in this file: "tmp/logger.log"
</br>


                    ====== Run script ======
* Run script from root folder of our project:
     <p> command: <i>python main.py</i> </p>

