from translate import Translator
translator= Translator(to_lang="german")
translation = translator.translate("i like to draw pictures")
print(translation)

from translate import Translator
translator= Translator(from_lang="german",to_lang="spanish")
translation = translator.translate("Ich zeichne gern")
print(translation)