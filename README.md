# Hệ thống gợi ý sản phẩm

Đây là một ứng dụng demo cho hệ thống gợi ý sản phẩm sử dụng kỹ thuật học máy. Hệ thống sẽ gợi ý sản phẩm dựa trên lịch sử mua sắm và lượt xem sản phẩm của người dùng.

## Dữ liệu

Dữ liệu bao gồm ba tệp CSV:

- `products.csv`: Chứa thông tin sản phẩm.
- `purchase_history.csv`: Chứa lịch sử mua sắm của người dùng.
- `product_views.csv`: Chứa lượt xem sản phẩm của người dùng.

## Các tệp

- `data/products.csv`
- `data/purchase_history.csv`
- `data/product_views.csv`
- `recommendation_model.py`

## Thiết lập

1. Đảm bảo bạn đã cài đặt Python trên hệ thống của mình.
2. Cài đặt các thư viện cần thiết bằng pip:

    ```sh
    pip install pandas scikit-learn
    ```

## Chạy script

1. Điều hướng đến thư mục dự án:

    ```sh
    cd /c:/Hmm/python/Demo
    ```

2. Chạy script mô hình gợi ý:

    ```sh
    python recommendation_model.py
    ```

## Kết quả

Script sẽ tải dữ liệu, huấn luyện mô hình gợi ý, đánh giá độ chính xác của mô hình và in ra các gợi ý sản phẩm cho một người dùng mẫu.

Ví dụ kết quả:

```
Loading datasets...
Datasets loaded successfully.
Merging datasets...
Datasets merged successfully.
Encoding categorical variables...
Categorical variables encoded successfully.
Preparing data for training...
Data prepared successfully.
Splitting data into training and testing sets...
Data split successfully.
Building and training the recommendation model...
Model trained successfully.
Evaluating the model...
Model accuracy: <accuracy_value>
Recommendations for user 1:
   product_id product_name    category
0           4     Sneakers       Shoes
1           5          Hat Accessories
2           1      T-shirt    Clothing
```

## Tùy chỉnh

Bạn có thể tùy chỉnh script để gợi ý sản phẩm cho các người dùng khác nhau bằng cách thay đổi `user_id` trong phần ví dụ sử dụng của script.

```python
# Ví dụ sử dụng
user_id = 1
recommendations = recommend_products(user_id)
print(f'Recommendations for user {user_id}:')
print(recommendations)
```

Thay thế `user_id = 1` bằng ID người dùng mong muốn để nhận gợi ý cho người dùng đó.

## Giải thích mô hình

Hệ thống gợi ý sản phẩm này sử dụng mô hình **Nearest Neighbors** (K-Nearest Neighbors - KNN) để gợi ý sản phẩm. Dưới đây là giải thích chi tiết về cách mô hình hoạt động và các bước thực hiện trong script.

### Mô hình Nearest Neighbors

Mô hình Nearest Neighbors là một thuật toán học máy không giám sát, được sử dụng để tìm các điểm dữ liệu gần nhất trong không gian đặc trưng. Trong ngữ cảnh của hệ thống gợi ý sản phẩm, mô hình này được sử dụng để tìm các sản phẩm tương tự mà người dùng có thể quan tâm dựa trên lịch sử mua sắm và lượt xem sản phẩm của họ.

### Các bước thực hiện trong script

1. **Tải dữ liệu**:
    - Script tải dữ liệu từ các tệp CSV `products.csv`, `purchase_history.csv`, và `product_views.csv`.

2. **Kết hợp dữ liệu**:
    - Dữ liệu từ các tệp CSV được kết hợp lại để tạo thành một tập dữ liệu duy nhất chứa thông tin về sản phẩm, lịch sử mua sắm và lượt xem sản phẩm.

3. **Mã hóa các biến phân loại**:
    - Các biến phân loại như `user_id` và `product_id` được mã hóa thành các giá trị số sử dụng `LabelEncoder`.

4. **Chuẩn bị dữ liệu cho huấn luyện**:
    - Dữ liệu được chia thành các đặc trưng (features) `X` và nhãn (labels) `y`.

5. **Chia dữ liệu thành tập huấn luyện và tập kiểm tra**:
    - Dữ liệu được chia thành tập huấn luyện và tập kiểm tra sử dụng `train_test_split`.

6. **Xây dựng và huấn luyện mô hình gợi ý**:
    - Mô hình Nearest Neighbors được xây dựng và huấn luyện trên tập dữ liệu huấn luyện.

7. **Đánh giá mô hình**:
    - Mô hình được đánh giá bằng cách tính toán độ chính xác của các gợi ý sản phẩm trên tập dữ liệu kiểm tra.

8. **Gợi ý sản phẩm**:
    - Hàm `recommend_products` được sử dụng để gợi ý sản phẩm cho một người dùng cụ thể dựa trên mô hình đã huấn luyện.
