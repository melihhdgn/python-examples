# ---------------------------------------------------------------------------------------------
"""
missing_report.py

Bu modülde veri setindeki eksik satırlar ve eksik değerler kontrol edilir.

• Eksik satırlar tespit edilir ve gerekli sütunlar eklenerek tamamlanır.
  Örneğin: 25. sütun mevcutken 167. satırda eksikse, o satıra 25. sütun eklenir.

• Veri setindeki tüm NULL değerleri için eksik veri raporu oluşturulur.

• 4 farklı sütundaki veriler ayrı ayrı TXT dosyaları olarak kaydedilir.
"""
# ---------------------------------------------------------------------------------------------
"""
outlier_detection.py

Bu modülde belirlenen 4 sütundaki aykırı değerler (outliers) çeşitli yöntemler kullanılarak tespit edilir.

• Tespit edilen aykırı değerler daha sonra düzenlenebilmesi için JSON formatında kaydedilir.

• Böylece veri temizleme işlemleri sırasında doğrudan bu JSON dosyası üzerinden işlem yapılabilir.
"""
# ---------------------------------------------------------------------------------------------
"""
fill_edit.py

Bu modül veri düzenleme işlemlerini içerir.

• İlk iki fonksiyon veri tiplerindeki uyumsuzlukları kontrol eder, düzeltir ve veri setini günceller.

• Sonraki dört fonksiyon ise:
  - all_outliers.json dosyasındaki kayıtları kullanır
  - boş (missing) ve aykırı (outlier) değerleri
  belirlenen yöntemlerle doldurur veya düzeltir.
"""
# ---------------------------------------------------------------------------------------------
"""
chart.py

Bu modül veri görselleştirme işlemleri için kullanılacaktır.

• Hangi sütun için hangi grafik türünün kullanılacağı burada tanımlanacaktır.

• Grafik ayarları ve görselleştirme işlemleri daha sonra bu dosyada düzenlenecektir.
"""
# ---------------------------------------------------------------------------------------------
"""
time_series.py

Bu modül veri setindeki belirli sütunları zaman serisi (time series) formatına dönüştürür.

• Zaman bilgisi içeren sütunlar uygun veri tipine çevrilir.
• Analiz ve modelleme için veri zaman serisi yapısına hazırlanır.
"""
# ---------------------------------------------------------------------------------------------
"""
scaling.py

Bu modül veri ölçeklendirme işlemlerini gerçekleştirir.

• Seçilen sütunlardaki değerler normalize edilerek 0 ile 1 arasına getirilir.

• Bu işlem özellikle makine öğrenmesi modelleri için veri hazırlığında kullanılır.
"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
"""
missing_report.py

This module handles missing data detection and reporting.

• Missing rows are identified and completed by adding the necessary columns.
  Example: If column 25 exists but row 167 is missing, column 25 is added to that row.

• A missing data report is generated for all NULL values in the dataset.

• Data from four selected columns are saved separately as TXT files.
"""
# ---------------------------------------------------------------------------------------------
"""
outlier_detection.py

This module detects outliers in four specified columns using different statistical methods.

• Detected outliers are saved in JSON format.

• This allows later data cleaning operations to directly reference the JSON file.
"""
# ---------------------------------------------------------------------------------------------
"""
fill_edit.py

This module is responsible for data correction and filling operations.

• The first two functions check and fix data type inconsistencies and update the dataset.

• The next four functions:
  - Use the records stored in all_outliers.json
  - Fill or correct missing and outlier values using predefined methods.
"""
# ---------------------------------------------------------------------------------------------
"""
chart.py

This module will be used for data visualization.

• It defines which type of chart should be used for which columns.

• Chart configurations and visualization logic will be implemented here.
"""
# ---------------------------------------------------------------------------------------------
"""
time_series.py

This module converts specified columns into time series format.

• Columns containing time information are converted to appropriate data types.

• The dataset is prepared for time series analysis and modeling.
"""
# ---------------------------------------------------------------------------------------------
"""
scaling.py

This module performs feature scaling operations.

• Selected columns are normalized so that their values fall between 0 and 1.

• This step is commonly used when preparing data for machine learning models.
"""
# ---------------------------------------------------------------------------------------------