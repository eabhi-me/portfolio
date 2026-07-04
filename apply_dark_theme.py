import re

# Files to edit
files = {
    'src/views/ProjectsView.vue': {
        'background: white;': 'background: transparent;',
        'background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);': 'background: transparent;',
        'color: #2c3e50;': 'color: #ffffff;',
        'color: #5a6c7d;': 'color: var(--text-secondary);',
        'color: rgb(5, 5, 5);': 'color: #ffffff;',
        'background: #f8f9fa;': 'background: rgba(255,255,255,0.03);',
        'background: white;': 'background: rgba(255,255,255,0.03);',
        'border: 1px solid #e9ecef;': 'border: 1px solid rgba(255,255,255,0.06);',
        'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);': 'background: var(--grad-main);',
        'background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);': 'background: rgba(255,255,255,0.06);',
        'color: #495057;': 'color: var(--text-secondary);',
        'color: #667eea;': 'color: #a78bfa;',
    },
    'src/views/SkillsView.vue': {
        'background: white;': 'background: transparent;',
        'background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);': 'background: transparent;',
        'color: #2c3e50;': 'color: #ffffff;',
        'color: #5a6c7d;': 'color: var(--text-secondary);',
        'color: #7f8c8d;': 'color: var(--text-muted);',
        'background: #f8f9fa;': 'background: rgba(255,255,255,0.03);',
        'background: #e9ecef;': 'background: rgba(255,255,255,0.04);',
        'border: 1px solid #e9ecef;': 'border: 1px solid rgba(255,255,255,0.06);',
        'border: 2px solid #667eea;': 'border: 2px solid #7c3aed;',
        'background: #f5f7fa;': 'background: rgba(255,255,255,0.02);',
        'color: #667eea;': 'color: #a78bfa;',
        'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);': 'background: var(--grad-main);',
    },
    'src/views/GitHubView.vue': {
        'background: white;': 'background: rgba(255,255,255,0.03);',
        'background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);': 'background: transparent;',
        'color: #2c3e50;': 'color: #ffffff;',
        'color: #5a6c7d;': 'color: var(--text-secondary);',
        'color: #7f8c8d;': 'color: var(--text-muted);',
        'background: #f8f9fa;': 'background: rgba(255,255,255,0.03);',
        'border: 1px solid #e9ecef;': 'border: 1px solid rgba(255,255,255,0.06);',
        'background: linear-gradient(180deg, var(--color-background) 0%, var(--color-background-soft) 100%);': 'background: transparent;',
    },
    'src/views/ContactView.vue': {
        'background: white;': 'background: transparent;',
        'background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);': 'background: transparent;',
        'color: #2c3e50;': 'color: #ffffff;',
        'color: #5a6c7d;': 'color: var(--text-secondary);',
        'color: #7f8c8d;': 'color: var(--text-muted);',
        'background: #f8f9fa;': 'background: rgba(255,255,255,0.03);',
        'border: 1px solid #e9ecef;': 'border: 1px solid rgba(255,255,255,0.06);',
        'border: 2px solid #e9ecef;': 'border: 2px solid rgba(255,255,255,0.08);',
        'color: #667eea;': 'color: #a78bfa;',
    },
    'src/views/ResumeView.vue': {
        'background: white;': 'background: rgba(255,255,255,0.03);',
        'background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);': 'background: transparent;',
        'color: #2c3e50;': 'color: #ffffff;',
        'color: #5a6c7d;': 'color: var(--text-secondary);',
        'color: #7f8c8d;': 'color: var(--text-muted);',
        'background: #f8f9fa;': 'background: rgba(255,255,255,0.03);',
        'border: 1px solid #e9ecef;': 'border: 1px solid rgba(255,255,255,0.06);',
        'background: #2c3e50;': 'background: #161827;',
        'color: #667eea;': 'color: #a78bfa;',
        'border-bottom: 2px solid #2c3e50;': 'border-bottom: 2px solid rgba(255,255,255,0.08);',
        'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);': 'background: var(--grad-main);',
    },
}

for filepath, replacements in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

print("\nDone updating styles!")
