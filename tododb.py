import pymysql


def get_tasks():
    get_sql="SELECT * FROM web_todo_list.todo"
    connection = pymysql.connect(user="root", password="toor",\
                                 host="localhost", database="web_todo_list")
    cursor = connection.cursor()
    cursor.execute(get_sql)
    results = cursor.fetchall()
    connection.close()
    return results


def add_task(task):
    insert_sql = "INSERT INTO web_todo_list.todo(task) VALUES (%s)"
    connection = pymysql.connect(user="root", password="toor",
                                 host="localhost", database="web_todo_list")
    cursor = connection.cursor()
    cursor.execute(insert_sql, (task,))
    connection.commit()
    connection.close()


def delete_task(task_id):
    delete_sql = "DELETE FROM web_todo_list.todo WHERE id=%s"
    connection = pymysql.connect(user="root", password="toor",
                                 host="localhost", database="web_todo_list")
    cursor = connection.cursor()
    cursor.execute(delete_sql, (task_id,))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    print(get_tasks())
    # add_task("test task2")
    print(get_tasks())
