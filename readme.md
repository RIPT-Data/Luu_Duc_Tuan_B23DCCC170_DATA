# <Lưu_Đức_Tuấn_B23DCCC170_DATA> Báo Cáo Tìm Hiểu Về Crawler Data.

## 1. Giới thiệu
Crawler data là kỹ thuật thu thập dữ liệu tự động từ các trang web, duyệt qua các trang web, phân tích nội dung, và trích xuất thông tin hữu ích. Công nghệ này được sử dụng rộng rãi trong nhiều lĩnh vực như thương mại điện tử, phân tích dữ liệu thị trường, nghiên cứu khoa học, và nhiều lĩnh vực khác.

## 2. Cách thức hoạt động
Crawler bắt đầu từ một URL gốc, sau đó tiếp tục duyệt qua các liên kết có trong trang để thu thập thông tin. Quy trình bao gồm các bước:
- Tải nội dung trang web (HTML).
- Phân tích nội dung và xác định dữ liệu cần thu thập.
- Trích xuất thông tin và lưu trữ vào định dạng phù hợp, như CSV, JSON, hay cơ sở dữ liệu.
- Lặp lại quy trình cho các trang tiếp theo dựa trên các liên kết.

## 3. Ứng dụng
Crawler data được ứng dụng trong nhiều lĩnh vực:
- **Theo dõi giá sản phẩm**: Các công ty thương mại điện tử sử dụng để theo dõi giá sản phẩm từ đối thủ.
- **Phân tích thị trường**: Thu thập thông tin từ mạng xã hội hoặc tin tức để phân tích xu hướng.
- **Tìm kiếm học thuật**: Crawler có thể được sử dụng để thu thập các bài báo nghiên cứu từ các trang web học thuật.

## 4. Nhược điểm
- **Luật pháp**: Việc thu thập dữ liệu từ một số trang có thể vi phạm điều khoản dịch vụ.
- **Xử lý dữ liệu**: Không phải dữ liệu nào cũng dễ trích xuất, đặc biệt khi trang web sử dụng nhiều JavaScript hoặc mã phức tạp.
- **Hiệu suất**: Crawler cần được tối ưu hóa để không gây quá tải cho trang web nguồn.

## 5. Python
Tạo một đoạn mã python đơn giản với thư viện requests, BeautifulSoup, csv để lấy dữ liệu từ https://vnexpress.net/ sau đó đọc và viết những dữ liệu cần thiết vào file csv.

```python
import  requests
from  bs4  import  BeautifulSoup
import  csv

url  =  "https://vnexpress.net/"
response  =  requests.get(url)

if  response.status_code  ==  200:
	soup  =  BeautifulSoup(response.text, 'html.parser')
	articles  =  soup.find_all('h3', class_='title-news')

	with  open('vnexpress_articles.csv', mode='w', newline='', encoding='utf-8') as  file:
		writer  =  csv.writer(file)
		writer.writerow(['Title', 'URL'])

		for  article  in  articles:
			title  =  article.text.strip()
			link  =  article.a['href']
			writer.writerow([title, link])

		print("'vnexpress_articles.csv' đã được lưu.")
```
Đoạn mã trên sẽ trả về file vnexpress_articles.csv.
