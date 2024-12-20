from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

def make_receipt(data, out_file_name=""):
    pdf = SimpleDocTemplate( out_file_name, pagesize = A4 ) 
    styles = getSampleStyleSheet() 
    title_style = styles[ "Heading1" ] 
    title_style.alignment = 1
    title = Paragraph( "receipt" , title_style ) 
    style = TableStyle( 
        [ 
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "BOX" , ( 0, 0 ), (6 , 6 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
        ] 
    ) 
    
    table = Table( data , style = style ) 
    pdf.build([ title , table ])  