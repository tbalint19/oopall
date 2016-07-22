from PIL import Image
from sqlhandling import Sql
from text import Text
from ui import UserInterface

picture = Image.new(UserInterface.createPicture())

for text_info in Sql.runSql():
    text = Text()
    text.calculate_length(picture)

Text.checkOccupyRatio()
Text.order_list()

for text in Text.ordered_list:
    picture = text.randomPlace(picture)

picture.save("ThirdOptionalAssingment10.png")