import pymysql.cursors
import pymysql

connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             password='salam1407',
                             database='Company',
                             charset = 'utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_table():
    with connection.cursor() as cursor:
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INT(11) PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                department VARCHAR(50) NOT NULL,
                salary int NOT NULL,
                gender VARCHAR(50) NOT NULL,
                age int,
                city VARCHAR(50)            
            )
        """
        cursor.execute(sql)
    connection.commit()
    print('Yaratıldı!')

# create_table()


def add_employee(name, department, salary, gender, age, city):
    with connection.cursor() as cursor:
        sql = "INSERT INTO employees (name, department, salary, gender, age, city) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, department, salary, gender, age, city))
    connection.commit()
    print('Employee yaratıldı')

# add_employee('John Doe', 'İT', 35000, 'Male', 25, 'London')
# add_employee('Mary Smith', 'HR', 45000, 'Female', 27, 'Mumbai')
# add_employee('James Brown', 'Finance', 50000, 'Male', 28, 'Delhi')
# add_employee('Mike Walker', 'Finance', 50000, 'Male', 28, 'London')
# add_employee('Linda Jones', 'HR', 75000, 'Female', 26, 'Mumbai')
# add_employee('Anurag Mohanty', 'İT', 35000, 'Male', 25, 'London')
# add_employee('Priyanla Dewangan', 'HR', 45000, 'Female', 27, 'Mumbai')
# add_employee('Sambit Mohanty', 'İT', 50000, 'Male', 28, 'London')
# add_employee('Pranaya Kumar', 'İT', 50000, 'Male', 28, 'London')
# add_employee('Hina Sharma', 'HR', 75000, 'Female', 26, 'Mumbai')


def get_employees():
    with connection.cursor() as cursor:
        sql = "select * from employees"

        cursor.execute(sql)
        
        result = cursor.fetchall()
        
        for eldeet in result:
            print(eldeet)

# get_employees()


def get_employee_for_id(employee_id):
    with connection.cursor() as cursor:
        sql = "select * from employees where id = %s"
        cursor.execute(sql, (employee_id))
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print("Məlumat yoxdur!")

# get_employee_for_id(5)

def get_employee_for_age(employee_age):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM employees WHERE age = %s"
        cursor.execute(sql, (employee_age))
        result = cursor.fetchall()
        if result:
            for a in result:
                print(a)

# get_employee_for_age(25)
# get_employee_for_age(26)

def get_employee():
    with connection.cursor() as cursor:
        sql = "select * from employees where department = %s and city = %s"
        cursor.execute(sql, ("Finance", "London"))
        result = cursor.fetchall()
        if result:
            for a in result:
                print(a)
        else:
            print("Məlumat yoxdur!")

# get_employee()

def update_employee(id, name, department, salary, gender, age, city):
    with connection.cursor() as cursor:
        sql = "update employees set name = %s, department = %s, salary = %s, gender = %s, age = %s, city = %s where id = %s"
        cursor.execute(sql, (name, department, salary, gender, age, city, id))
    connection.commit()
    print(cursor.rowcount, "məlumat yeniləndi!")

# update_employee(1, "John Doe", "IT", 45000, "Male", 30, "New York")


def delete_employee_for_salary(salary):
    with connection.cursor() as cursor:
        sql = "delete from employees where salary = %s"
        cursor.execute(sql, (salary,))
        print(cursor.rowcount, "məlumat Silindi!")
    connection.commit()


# delete_employee_for_salary(45000)


def delete_employee_for_department(department):
    with connection.cursor() as cursor:
        sql = "delete from employees where department = %s"
        cursor.execute(sql, (department,))
        print(cursor.rowcount, "məlumat Silindi!")
    connection.commit()

# delete_employee_for_department("IT")


def delete_employees():
    with connection.cursor() as cursor:
        sql = "DELETE FROM employees"
        cursor.execute(sql)
        print("Bütün Məlumatlar silindi!")
    connection.commit()

# delete_employees()

def delete_table():
    with connection.cursor() as cursor:
        sql = "drop table if exists employees"
        cursor.execute(sql)
        print("Table silindi!")
    connection.commit()


# delete_table()


def delete_database():
    with connection.cursor() as cursor:
        sql = "drop database if exists Company"
        cursor.execute(sql)
        print("Database silindi!")
    connection.commit()

# delete_database()

