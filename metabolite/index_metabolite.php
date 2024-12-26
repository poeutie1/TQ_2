<?php

$command = 'python3 app.py';
$output = shell_exec($command);
$data = json_decode($output, true);

?>
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/TQ/Python/static/styles.css">
    #ここのアドレスも変更する
    <title>Metabolite Structure</title>
</head>

<body>
    <div class="dm">
        <?php foreach ($data as $category => $subcategories): ?>
        <details>
            <summary><strong><?php echo htmlspecialchars($category); ?></strong></summary>
            <ul class="menu-tree">
                <?php foreach ($subcategories as $subcategory => $molecules): ?>
                <details>
                    <summary><?php echo htmlspecialchars($subcategory); ?></summary>
                    <?php foreach ($molecules as $molecule): ?>
                    <div >
                        <?php foreach ($molecule as $key => $value): ?>
                            
                        <span class="hover-text" data-text="<?php echo htmlspecialchars($key); ?>">
                            <?php echo htmlspecialchars($value); ?>
                        </span>
                        <?php endforeach; ?>
                    </div>
                    <?php endforeach; ?>
                </details>
                <?php endforeach; ?>
            </ul>
        </details>
        <?php endforeach; ?>
    </div>
</body>

</html>
